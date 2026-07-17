import APIURL from "../services/api";

export async function DownlaodFile(filename){

    const  response = await APIURL.get(`/download${filename}`,{
        responseType: 'blob'
    })

    const url = window.URL.createObjectURL(response.data)
    const link = document.createElement('a')

    link.href = url
    link.download = filename

    document.body.appendChild(link)

    link.click()
    link.remove()

    window.URL.revokeObjectURL(url)
}