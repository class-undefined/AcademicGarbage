<script lang="ts" setup>
import { Check } from '@element-plus/icons-vue';
</script>

<template>
    <div>
        <el-progress type="circle" :percentage="100" status="success">
            <el-button type="success" :icon="Check" circle />
        </el-progress>
    </div>
</template>

<style lang="scss">
//
</style>
