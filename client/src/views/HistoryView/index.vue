<script lang="ts" setup>
import { ref, onMounted } from "vue"
import { useGlobalStore } from '@/store/global';
import Panel from "@/views/HistoryView/Panel.vue"
import TodayLine from "@/views/HistoryView/TodayLine/index.vue"
import Title from "@comps/Title.vue"
//

</script>

<template>
    <div class="history-view">
        <Title value="仪表板" :padding="[0, 0]" />
        <panel />
        <el-divider />
        <Title value="频率" :padding="[0, 0]" />
        <today-line class="today-line" />
        <el-divider />
        <Title value="历史记录" :padding="[0, 0]" />
    </div>
</template>

<style lang="scss">
.history-view {
    padding: 10px 20px;
}

.today-line {
    width: 100%;
    height: 350px;
}
</style>
