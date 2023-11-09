$(document).ready(function () {
    // 这里引入编辑器的配置文件代码

    ClassicEditor
        .create(document.querySelector('#id_content'))
        .then(editor => {
            console.log(editor);
        })
        .catch(error => {
            console.error(error);
        });

})