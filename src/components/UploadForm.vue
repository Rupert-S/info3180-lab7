<template>
     <form @submit.prevent="uploadPhoto" class="uploadForm" id="uploadForm" >
        <label for="photo">Photo:</label>
        <input type="file" id="photo" name="photo">
        <label for="description">Description:</label>
        <input type="text" id="description" name="description">
        <button class="btn btn-primary mb-2">Submit</button>
    </form> 
</template>

<script>
export default {
    data() {
        return {
            csrf_token: '',
            message:[], error:[]
        }
    },
    created() {
        this.getCsrfToken();
    },
    methods: {
        uploadPhoto() {
            let uploadForm = document.getElementById('uploadForm');
            let form_data = new FormData(uploadForm);
            let self = this;
            fetch("/api/upload", {
                method: 'POST',
                body: form_data,
                headers: {
                    'X-CSRFToken': this.csrf_token
                }
            })  
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                // display a success message
                console.log(data);
                self.message = data.message;
            })
            .catch(function (error) {
                console.log(error);
                self.error = error;
            });
        },
        getCsrfToken() {
            let self = this;
            fetch('/api/csrf-token')
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                self.csrf_token = data.csrf_token;
            })
        }
    }
}
</script>