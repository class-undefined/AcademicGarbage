<script lang="ts" setup>
import { useGlobalStore } from "@/store/global"
import { ref } from "vue"
import { useLoading } from "@utils/base"
import { useRouter } from "vue-router"
import { showLoadingToast } from "vant"
const username = ref("")
const password = ref("")
const [loading, setLoading] = useLoading()
const router = useRouter()
const onSubmit = () => {
    const global = useGlobalStore()
    setLoading(true)
    const toast = showLoadingToast({
        message: "正在登录",
        forbidClick: true,
    })
    global
        .login(username.value, password.value)
        .then(() => {
            router.push("/")
        })
        .finally(() => {
            setLoading(false)
            toast.close()
        })
}
</script>

<template>
    <div class="login-form">
        <van-form @submit="onSubmit">
            <van-cell-group inset>
                <van-field
                    v-model="username"
                    name="用户名"
                    label="用户名"
                    placeholder="用户名"
                    :rules="[{ required: true, message: '请填写用户名' }]"
                />
                <van-field
                    v-model="password"
                    type="password"
                    name="密码"
                    label="密码"
                    placeholder="密码"
                    :rules="[{ required: true, message: '请填写密码' }]"
                />
            </van-cell-group>
            <div style="margin: 16px">
                <van-button round block :loading="loading" type="primary" native-type="submit">
                    登录
                </van-button>
            </div>
        </van-form>
    </div>
</template>

<style lang="scss">
.login-form {
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 100vh;
}
</style>
