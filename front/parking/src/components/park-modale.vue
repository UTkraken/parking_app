<template>
    <div class="modale-container" v-if="revele">
        <div class="exit" v-on:click="toggleModale">X</div>
        <div v-if="loading">Loading...</div>
        <div v-else-if="error">Error: {{ error }}</div>
        <div v-else:"parkingData">
            <h2>{{ parkingData.name }}</h2>
            <hr>
            <p>Number of floors: {{ parkingData.floor_count }}</p>
            <p>Number of spots: {{ parkingData.spot_count }}</p>
        </div>
    </div>
</template>

<script>
export default {
    name: "ParkModale",
    props: {
        revele: Boolean,
        toggleModale: Function,
        parkingId: String,
    },
    data() {
        return {
            parkingData: null,
        };
    },
    watch: {
        revele(newVal) {
            if (newVal) {
                this.fetchParkingData(this.parkingId);
            }
        },
    },
    methods: {
        async fetchParkingData(parkingId) {
            try {
                const response = await fetch(`http://localhost:8000/api/parkings/${parkingId}`);
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                this.parkingData = await response.json();
            } catch (error) {
                console.error("Error fetching parking data:", error);
            }
        },
    }
}
</script>

<style scoped>
.modale-container {
    position: fixed;
    top: 20%;
    left: 30%;
    width: 40%;
    height: 60%;
    background-color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #7D7D7D;
    border-radius: 15px;
    z-index: 1000;
    border: 1px solid #7D7D7D;
    box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
    font-family: 'Lato';
    text-align: center;
}

.exit {
    position: absolute;
    top: 10px;
    right: 20px;
    cursor: pointer;
    font-size: 20px;
    color: #FD8074;
}

h2 {
    font-size: 1.5em;
    font-weight: bold;
    text-transform: uppercase;
}

p {
    margin-bottom: 5%;
}

</style>