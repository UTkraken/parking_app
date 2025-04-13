import axios from "axios"

const api = axios.create({
  baseURL: "http://localhost:8000/api",
})

export function getParkings() {
    return api.get("/parkings")
}