<script lang="ts" setup>
import { ref, onMounted } from "vue"
import { useGlobalStore } from '@/store/global';
import Panel from "@/views/HistoryView/Panel.vue"
import Title from "@comps/Title.vue"
//

</script>

<template>
    <div class="history-view">
        <Title value="仪表板" :padding="[0, 0]" />
        <panel />
    </div>
</template>

<style lang="scss">
.history-view {
    padding: 10px 20px;
}
</style>
