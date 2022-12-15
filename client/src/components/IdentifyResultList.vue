<script lang="ts" setup>
import { ref, onMounted } from "vue"
import { getGateWay } from '@/socket';
import { Photo } from "@/types/photo";
const photos = ref<Photo[]>([])
const loading = ref(false)
const gateway = getGateWay()
gateway.then(socket => {
    socket.on("accept_identify_rst", (result) => {
        if (result.code !== 20000) return
        const photo = result.data.data
        photos.value.push(photo)
    })
})
</script>

<template>
    <van-list v-model:loading="loading" :finished="!loading" finished-text="没有更多了">
        <van-cell v-for="photo in photos" :key="photo.id">
            <van-image width="100%" height="100%" :src="photo.processed_url" />
        </van-cell>
    </van-list>
</template>

<style lang="scss">
//
</style>
