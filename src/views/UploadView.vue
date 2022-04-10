<template>
    <div class="upload container">
        <h2>Upload Photo</h2>
        <UploadForm />
    </div>
</template>

<script>
    import UploadForm from '@/components/UploadForm.vue'
    export default {
        data() {
            return {};
        },
        components: { UploadForm }
    };
</script>
