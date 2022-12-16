<script lang="ts" setup>
import { ref, onMounted } from "vue"
import { useGlobalStore } from '@/store/global';
const global = useGlobalStore()
const totalAccuracy = ref(0) // 所有图片的平均准确度
const todayCount = ref(0) // 今天创建总数
const todayAccuracy = ref(0) // 今天图片的平均准确度
onMounted(() => {
    global.user!.refreshPhotos().then(_ => {
        totalAccuracy.value = global.user!.totalAccuracy() * 100
        const todayPhotos = global.user!.getTodayPhotos()
        todayCount.value = todayPhotos.length
        todayAccuracy.value = global.user!.todayAccuracy() * 100
    })
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
    <div class="panel-container">
        <div>
            <el-progress type="circle" :width="100" :percentage="todayAccuracy.toFixed(2)" :colors="colors">
                <template #default="{ percentage }">
                    <span class="percentage-value-edge">{{ percentage }}%</span>
                    <span class="percentage-label-edge">今日精准率</span>
                </template>
            </el-progress>
            <el-progress type="circle" :percentage="100" status="success">
                <template #default>
                    <span class="percentage-value-center">{{ todayCount }}</span>
                    <span class="percentage-label-center">今日识别数</span>
                </template>
            </el-progress>
            <el-progress type="circle" :width="100" :percentage="totalAccuracy.toFixed(2)" :colors="colors">
                <template #default="{ percentage }">
                    <span class="percentage-value-edge">{{ percentage }}%</span>
                    <span class="percentage-label-edge">总精准率</span>
                </template>
            </el-progress>
        </div>
    </div>
</template>

<style lang="scss">
.panel-container {
    width: 100%;
    display: flex;
    justify-content: center;
}

.percentage-value-edge {
    display: block;
    margin-top: 10px;
    font-size: 20px;
}

.percentage-label-edge {
    display: block;
    margin-top: 10px;
    font-size: 12px;
}

.percentage-value-center {
    display: block;
    margin-top: 10px;
    font-size: 28px;
}

.percentage-label-center {
    display: block;
    margin-top: 10px;
    font-size: 12px;
}
</style>
