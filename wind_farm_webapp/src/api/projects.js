import apiClient from "./client"

export const getAll = () => {
  return apiClient.get(`/projects/`)
}
