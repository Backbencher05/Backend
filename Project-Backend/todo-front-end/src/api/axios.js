import axios from "axios";

const baseURL = "http://localhost:8000/api/";

const axiosInstance = axios.create({
  baseURL,
  timeout: 5000,
  headers: {
    Authorization: localStorage.getItem("access")
      ? "Bearer " + localStorage.getItem("access")
      : null,
    "Content-Type": "application/json",
    accept: "application/json",
  },
});

// 🔁 Add interceptor for auto token refresh
axiosInstance.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    // If token has expired and we haven’t retried already
    if (
      error.response?.status === 401 &&
      error.response?.data?.code === "token_not_valid" &&
      !originalRequest._retry
    ) {
      originalRequest._retry = true;

      try {
        const refresh = localStorage.getItem("refresh");

        const res = await axios.post(`${baseURL}token/refresh/`, {
          refresh,
        });

        localStorage.setItem("access", res.data.access);

        axiosInstance.defaults.headers["Authorization"] =
          "Bearer " + res.data.access;
        originalRequest.headers["Authorization"] =
          "Bearer " + res.data.access;

        return axiosInstance(originalRequest); // Retry original request
      } catch (refreshError) {
        console.log("Refresh token failed", refreshError);
        window.location.href = "/login"; // Optional: auto logout
        return Promise.reject(refreshError);
      }
    }

    return Promise.reject(error);
  }
);

export default axiosInstance;
