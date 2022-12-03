<script lang="ts" setup>
import { routes } from "@router/index"
import { useRouter } from "vue-router"
import { watch, ref, computed } from "vue"
const router = useRouter()

const tabs = routes
    .filter(route => route?.meta?.navbar)
    .map(route => {
        return {
            title: route.meta?.title as string,
            icon: route.meta?.icon as undefined,
        }
    })

const current = ref(router.currentRoute.value)
watch(
    () => router.currentRoute.value,
    to => {
        current.value = to
    },
    { immediate: true, deep: true }
)
const tabHeight = computed(() => {
    if (current.value.meta?.navbar) return 50
    return 0
})
</script>

<template>
    <div class="main" :style="{ height: `calc(100% - ${tabHeight}px)` }"><RouterView /></div>
    <div>
        <van-tabbar v-if="current.meta?.navbar" v-model="current.path">
            <van-tabbar-item v-for="tab in tabs" :key="tab.title" :icon="tab.icon">
                {{ tab.title }}
            </van-tabbar-item>
        </van-tabbar>
    </div>
</template>

<style lang="scss">
.main {
    height: 100%;
    width: 100%;
}
</style>
