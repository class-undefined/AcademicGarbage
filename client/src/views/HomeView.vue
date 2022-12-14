<script lang="ts" setup>
import { ref, onMounted } from "vue"
import Title from "@comps/Title.vue"
import { ElUpload, ElIcon, ElButton, UploadProps, UploadUserFile, ElDialog, UploadInstance } from "element-plus"
import { Plus } from "@element-plus/icons-vue"
import { getToken } from "@/utils/api/auth/auth";
import { requestConfig } from "@/request.config";
import { showLoadingToast, showSuccessToast, showFailToast } from "vant";
import { ToastWrapperInstance } from "vant/lib/toast/types";
import { useLoading } from "@/utils/base";
import { getGateWay } from "@/socket";
const photos = ref<UploadUserFile[]>([])
const dialogImageUrl = ref("")
const dialogVisible = ref(false)
const action = requestConfig.baseUrl + "user/add_photo"
const uploadRef = ref<UploadInstance>()
const [loading, setLoading] = useLoading()
const afterRead = () => {
    // 此时可以自行将文件上传至服务器
}
const handleRemove: UploadProps["onRemove"] = (uploadFile, uploadFiles) => {
    console.log(uploadFile, uploadFiles)
}

const handlePictureCardPreview: UploadProps["onPreview"] = uploadFile => {
    dialogImageUrl.value = uploadFile.url!
    dialogVisible.value = true
}
const getUploaderHooks = () => {
    let toast: ToastWrapperInstance | null = null
    const onSuccess = () => {
        if (toast) toast.close()
        setLoading(false)
        showSuccessToast("上传成功")
    }
    const onError = () => {
        if (toast) toast.close()
        setLoading(false)
        showFailToast("上传失败")
    }
    const submit = () => {
        toast = showLoadingToast("正在上传")
        setLoading(true)
        uploadRef.value!.submit()
    }
    return { submit, onSuccess, onError }
}
const { submit, onSuccess, onError } = getUploaderHooks()

const headers = {
    Token: getToken()
}

onMounted(() => {
    const gateway = getGateWay()
    gateway.connect()
})

</script>

<template>
    <Title value="安全帽识别" />
    <div class="uploader">
        <div style="max-width: 316px;">
            <el-upload class="uploader-instance" :on-success="onSuccess" :on-error="onError" :headers="headers"
                name="image" :v-model:file-list="photos" :action="action" list-type="picture-card" :auto-upload="false"
                ref="uploadRef" :on-preview="handlePictureCardPreview" :on-remove="handleRemove">
                <el-icon>
                    <Plus />
                </el-icon>
            </el-upload>
        </div>
    </div>
    <div class="upload-btn-box">
        <van-button block type="primary" @click="submit" :loading="loading">上传并识别</van-button>
    </div>
    <el-dialog v-model="dialogVisible">
        <img w-full :src="dialogImageUrl" alt="Preview Image" />
    </el-dialog>
</template>

<style lang="scss">
.uploader {
    width: 100%;
    display: flex;
    flex-direction: row;
    margin: 0 auto;
    justify-content: center;
}

.uploader-instance {
    display: flex;
    flex-direction: row;
    justify-content: center;


}

.upload-btn-box {
    height: 80px;
    padding: 20px 0;
}
</style>
