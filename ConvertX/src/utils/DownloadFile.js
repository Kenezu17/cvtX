import APIURL from "../services/api";

export async function DownlaodFile(filename) {
    try {
        const response = await APIURL.get(`/download/${filename}`, {
            responseType: 'blob'
        });

        const url = window.URL.createObjectURL(response.data);
        const link = document.createElement('a');

        link.href = url;
        link.download = filename;

        document.body.appendChild(link);
        link.click();
        link.remove();

        window.URL.revokeObjectURL(url);
        return { success: true, message: 'Download started' };
    } catch (error) {
        return {
            success: false,
            message: error?.response?.data?.detail || 'Download failed'
        };
    }
}