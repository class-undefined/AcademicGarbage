<script lang="ts" setup>
import { ref, onMounted } from "vue"
import { useGlobalStore } from '@/store/global';
const global = useGlobalStore()
const totalAccuracy = ref(0)
onMounted(() => {
    global.user!.refreshPhotos().then(_ => totalAccuracy.value = global.user!.totalAccuracy() * 100)
})
const colors = [
    { color: '#f56c6c', percentage: 20 },
    { color: '#e6a23c', percentage: 40 },
    { color: '#5cb87a', percentage: 60 },
    { color: '#1989fa', percentage: 80 },
    { color: '#6f7ad3', percentage: 100 },
]

</script>

<template>
    <div>
        <el-progress type="circle" :percentage="totalAccuracy.toFixed(2)" :colors="colors">
            <template #default="{ percentage }">
                <span class="percentage-value">{{ percentage }}%</span>
                <span class="percentage-label">平均精准率</span>
            </template>
        </el-progress>
    </div>
</template>

<style lang="scss">
.percentage-value {
    display: block;
    margin-top: 10px;
    font-size: 28px;
}

.percentage-label {
    display: block;
    margin-top: 10px;
    font-size: 12px;
}
</style>
