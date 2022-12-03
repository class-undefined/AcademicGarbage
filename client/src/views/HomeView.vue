<script lang="ts" setup>
import { ref } from "vue"
import Title from "@comps/Title.vue"
import { ElUpload, ElIcon, ElButton, UploadProps, UploadUserFile, ElDialog } from "element-plus"
import { Plus } from "@element-plus/icons-vue"
const photos = ref<UploadUserFile[]>([])
const dialogImageUrl = ref("")
const dialogVisible = ref(false)
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
</script>

<template>
    <Title value="上传图片" />
    <el-upload
        :v-model:file-list="photos"
        action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
        list-type="picture-card"
        :on-preview="handlePictureCardPreview"
        :on-remove="handleRemove"
    >
        <el-icon><Plus /></el-icon>
    </el-upload>
    <el-dialog v-model="dialogVisible">
        <img w-full :src="dialogImageUrl" alt="Preview Image" />
    </el-dialog>
</template>

<style lang="scss">
.uploader {
    display: flex;
    justify-content: center;
}
</style>
