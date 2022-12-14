import { Photo } from "@/types/photo"

export type EventsHandle = {
    identify: (photo: Photo) => void
}