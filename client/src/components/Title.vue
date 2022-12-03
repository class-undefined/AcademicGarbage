<script lang="ts" setup>
import { computed } from "vue"
const props = defineProps<{
    value: string
    padding?: [number, number]
    height?: number
}>()
const height = `${props.height || 48}px`
const padding = computed(() => {
    const v = props.padding ?? [10, 16]
    return `${v[0]}px ${v[1]}px`
})
console.log(padding.value)
</script>

<template>
    <div :style="{ height, padding }" class="title">
        <span>{{ props.value }}</span>
    </div>
</template>

<style scoped lang="scss">
.title {
    box-sizing: border-box;
    color: #969799;
    display: flex;
    font-size: 14px;
    font-weight: 400;
    flex-direction: column;
    justify-content: center;
}
</style>
