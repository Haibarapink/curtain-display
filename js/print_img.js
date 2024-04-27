window.onload = function() {
    const imgContainer = document.getElementById('product-container-id');
    console.log(imgContainer);
    const folderPath = '/images/curtain_img'
    fetch(folderPath)
        .then(res => res.text())
        .then(text => {
            const parser = new DOMParser();
            const xmlDoc = parser.parseFromString(text, 'text/xml');

            // 获取所有图片文件的名称
            const files = xmlDoc.getElementsByTagName('a');
            const imageFiles = Array.from(files).filter(file => file.textContent.match(/\.(jpg|jpeg|png|gif)$/));
            console.log(imageFiles);
        })
}