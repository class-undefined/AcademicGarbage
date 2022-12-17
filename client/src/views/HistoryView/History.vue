<script lang="ts" setup>
import { ref, onMounted, computed, ComputedRef } from "vue"
import { Photo } from "@/types/photo";
import { useGlobalStore } from "@/store/global";
import { showImagePreview, showNotify } from 'vant';
const gloabl = useGlobalStore()
const photos: ComputedRef<Photo[]> = computed(() => gloabl.user?.photos ?? [])
const loading = ref(false)
const handleClick = (photo: Photo) => {
    if (photo.processed_url) showImagePreview([photo.processed_url])
    else {
        showNotify({ type: 'warning', message: '该图片似乎并不含有安全帽' })
        showImagePreview([photo.original_url])
    }
}
</script>

<template>
    <van-list v-model:loading="loading" :finished="!loading" finished-text="没有更多了">
        <van-cell @click="handleClick(photo)" center is-link value="查看结果" :label="photo.create_time.toDateString()"
            v-for="photo in photos" :key="photo.id">
            <template #title>
                <!-- <span class="custom-title">单元格</span> -->
                <van-tag type="primary">{{ photo.helmets_count }}</van-tag>
                <van-tag type="success">{{ photo.accuracy }}</van-tag>
            </template>
        </van-cell>
    </van-list>
</template>

<style lang="scss">
//
</style>
