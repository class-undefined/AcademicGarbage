<script lang="ts" setup>
import { ref, onMounted, computed } from "vue"
import Title from "@comps/Title.vue"
import { ElUpload, ElIcon, ElButton, UploadProps, UploadUserFile, ElDialog, UploadInstance, UploadFile, UploadFiles } from "element-plus"
import { Plus } from "@element-plus/icons-vue"
import { getToken } from "@/utils/api/auth/auth";
import { requestConfig } from "@/request.config";
import { showLoadingToast, showSuccessToast, showFailToast } from "vant";
import { ToastWrapperInstance } from "vant/lib/toast/types";
import { useLoading } from "@/utils/base";
import { getGateWay } from "@/socket";
const photos = ref<UploadUserFile[]>([])
const disableUploadBtn = ref(true)
const dialogImageUrl = ref("")
const dialogVisible = ref(false)
const action = requestConfig.baseUrl + "user/add_photo"
const uploadRef = ref<UploadInstance>()
const [loading, setLoading] = useLoading()
const afterRead = () => {
    // 此时可以自行将文件上传至服务器
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
        uploadRef.value!.clearFiles(["success"])
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

const onChange = (uploadFile: UploadFile, uploadFiles: UploadFiles) => {
    disableUploadBtn.value = uploadFiles.length === 0
}

const onRemove = (uploadFile: UploadFile, uploadFiles: UploadFiles) => {
    disableUploadBtn.value = uploadFiles.length === 0
}

const headers = {
    Token: getToken()
}

onMounted(() => {
    const gateway = getGateWay()
    gateway.connect()
})

</script>

<template>
    <div class="home-view">
        <Title value="安全帽识别" :padding="[0, 0]" />
        <div class="uploader">
            <div style="max-width: 316px;">
                <el-upload class="uploader-instance" :on-change="onChange" :on-success="onSuccess" :on-error="onError"
                    :headers="headers" name="image" :v-model:file-list="photos" :action="action"
                    list-type="picture-card" :auto-upload="false" ref="uploadRef" :on-preview="handlePictureCardPreview"
                    :on-remove="onRemove">
                    <el-icon>
                        <Plus />
                    </el-icon>
                </el-upload>
            </div>
        </div>
        <div class="upload-btn-box">
            <van-button block type="primary" @click="submit" :loading="loading"
                :disabled="disableUploadBtn">上传并识别</van-button>
        </div>
        <el-divider />
        <van-image-preview v-model:show="dialogVisible" :images="[dialogImageUrl]" />

    </div>
</template>

<style lang="scss" scoped>
.home-view {
    padding: 10px 20px;
}

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
    padding-top: 20px;
}
</style>
