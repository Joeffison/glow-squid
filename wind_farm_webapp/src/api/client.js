import axios from "axios";

const axiosInstance = axios.create({
  baseURL: `${process.env.REACT_APP_WIND_FARM_API}/api/v1`
})

export default axiosInstance;
