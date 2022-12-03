import { Ref, ref } from "vue"
/**
 * 加载状态hook
 * @returns [loading, setLoading]
 */
export const useLoading = (): [Ref<boolean>, (val: boolean) => boolean] => {
    const value = ref(false)
    const setVal = (val: boolean) => (value.value = val)
    return [value, setVal]
}
