export function getFileIcon(filename) {
    const extension = filename.split(".").pop().toLowerCase();

    switch (extension) {
        case "pdf":
            return "📕";

        case "docx":
            return "📘";

        case "xlsx":
            return "📗";

        case "png":
        case "jpg":
        case "jpeg":
            return "🖼️";

        default:
            return "📄";
    }
}