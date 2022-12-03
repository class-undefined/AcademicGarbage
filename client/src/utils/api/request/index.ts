/** 发起欲加载，利用浏览器的图片缓存机制（相同url资源只会请求服务器加载一次）
 * @param src: 图片路径
 * @param timeout: 等待时间 default: 5000
 * 成功交付则继续返回传递进来的图片路径
 */
export const loadImage = (src: string, timeout: number = 10000) => {
    return new Promise<string>((resolve, reject: (reason: string) => void) => {
        const img = new Image() as HTMLImageElement | null
        if (!img) return
        img.src = src
        img.onload = (e) => {
            e.preventDefault()
            e.stopPropagation()
            resolve(src)
        }
        if (img) img.onerror = () => reject("Image loading fail!")
        setTimeout(() => reject("Image loading timeout!"), timeout)
    })
}