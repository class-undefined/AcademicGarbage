<script lang="ts" setup>
import { useGlobalStore } from "@/store/global"
import { ref } from "vue"
import { useLoading } from "@utils/base"
import { useRouter } from "vue-router"
import { showFailToast, showLoadingToast } from "vant"
const username = ref("")
const password = ref("")
const passwordCheckd = ref("")
const [loading, setLoading] = useLoading()
const router = useRouter()
const onSubmit = () => {
    username.value = username.value.trim()
    password.value = password.value.trim()
    passwordCheckd.value = passwordCheckd.value.trim()
    if (username.value.length < 8) {
        showFailToast("账号长度不得小于8位")
        return 
    }
    if (password.value.length < 8) {
        showFailToast("密码长度不得小于8位")
        return 
    }
    if (password.value !== passwordCheckd.value) {
        showFailToast("两次输入密码不一致")
        return 
    }
    const global = useGlobalStore()
    setLoading(true)
    const toast = showLoadingToast({
        message: "正在注册",
        forbidClick: true,
    })
    global
        .register(username.value, password.value)
        .then(() => {
            router.push("/login")
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
                <van-field
                    v-model="passwordCheckd"
                    type="password"
                    name="再次输入密码"
                    label="再次输入密码"
                    placeholder="再次输入密码"
                    :rules="[{ required: true, message: '请再次输入密码' }]"
                />
            </van-cell-group>
            <div style="margin: 16px">
                <van-button round block :loading="loading" type="primary" native-type="submit">
                    注册
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
.register-btn {
    font-size: 12px;
    color: #f5f5f5;

}
</style>
