$(document).ready(function () {
    //重点代码 适配器
    class UploadAdapter {
        constructor(loader) {
            this.loader = loader;
        }

        upload() {
            return new Promise((resolve, reject) => {
                const data = new FormData();
                let file = [];
                //this.loader.file 这是一个Promise格式的本地文件流，一定要通过.then 进行获取，之前在各大博客查了很多文章都拿不到这个值，最后经过两个多小时的探索终于找到了是Promise问题。
                this.loader.file.then(res => {
                    file = res; //文件流
                    data.append('file', file); //传递给后端的参数，参数名按照后端需求进行填写
                    // data.append('type','1');
                    data.append('bucketName', 'xydms');
                    //传递给后端的参数，参数名按照后端需求进行填写
                    data.append('ckCsrfToken', 'oCS0feM9aUb0v4zQqrEgcExpQeWTZXG4pch37uds');
                    //传递给后端的参数，参数名按照后端需求进行填写
                    data.append('objectName', '1101053001');
                    //传递给后端的参数，参数名按照后端需求进行填写
                    $.ajax({
                        url: 'http://xxx/xxx.php', //后端的上传接口
                        type: 'POST',
                        data: data,
                        dataType: 'json',
                        processData: false,
                        contentType: false,
                        success: function (data) {
                            if (data) {
                                console.log(data)
                                resolve({
                                    default: data.default //后端返回的参数 【注】返回参数格式是{uploaded:1,default:'http://xxx.com'}
                                });
                            } else {
                                reject(data.msg);
                            }
                        }
                    });
                })

            });
        }
        abort() {
        }
    }


    // 这里引入编辑器的配置文件代码
    ClassicEditor
        .create(document.querySelector('#id_content'), {
            // ckfinder: {
            // 	uploadUrl: 'upload'
            // },
            toolbar: {
                items: [
                    'heading',
                    '|',
                    'bold',
                    'italic',
                    'link',
                    'bulletedList',
                    'numberedList',
                    '|',
                    'indent',
                    'outdent',
                    '|',
                    'imageUpload',
                    'blockQuote',
                    'insertTable',
                    'mediaEmbed',
                    'undo',
                    'redo'
                ]
            },
            language: 'zh',
            image: {
                toolbar: [
                    'imageTextAlternative',
                    'imageStyle:full',
                    'imageStyle:side'
                ]
            },
            table: {
                contentToolbar: [
                    'tableColumn',
                    'tableRow',
                    'mergeTableCells'
                ]
            },
            licenseKey: '',

        })
        .then(editor => {
            console.log(editor);
        })
        .catch(error => {
            console.error(error);
        });

})