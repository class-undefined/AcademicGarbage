<script lang="ts" setup>
import { useGlobalStore } from "@/store/global";
import { onMounted, ref, watch, computed } from "vue"
import * as echarts from "echarts"
import { createLineOption } from "./options";
const data = computed(() => {
    const global = useGlobalStore()
    const todayPhotos = global.user?.getTodayPhotos() ?? []
    const counts = new Array<number>(24).fill(0)
    for (const photo of todayPhotos) {
        const hours = photo.create_time.getHours()
        counts[hours]++
    }
    return counts
})
const labels = new Array<string>(24)
for (let i = 0; i < labels.length; i++) {
    labels[i] = `${i}:00`
}
const dom = ref()
onMounted(() => {
    const chart = echarts.init(dom.value)
    chart.setOption(createLineOption(labels, data.value))
})
</script>

<template>
    <div class="line-chart" ref="dom"></div>
</template>

<style lang="scss">
.line-chart {
    width: 100%;
    height: 100%;
}
</style>
