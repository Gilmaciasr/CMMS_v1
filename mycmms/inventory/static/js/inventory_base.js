
const list_devices = async () => {
    try {
        const response = await fetch('http://127.0.0.1:8000/inventory/inventory/');
        const data = await response.json();
        console.log(data);
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async() => {
    await list_devices();
});