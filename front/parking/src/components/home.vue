<template>
  <div>
    <modale v-bind:revele="revele" v-bind:toggleModale="toogleModale" v-bind:parking-id="selectedParkingId"></modale>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error">Error: {{ error }}</div>
    <div v-else class="home-container">
      <h1>Available Parking</h1>
      <div class="park-container">
        <div class="park-box" v-on:click="toogleModale(parking.id)" v-for="parking in parkings" :key="parking.id">
          <p>{{ parking.name }}</p>
        </div>
      </div>
      <button v-on:click="redirectReservation" class="new-resa-button">New reservation</button>
    </div>
  </div>
</template>
  
<script>
  import { ref, onMounted } from 'vue'
  import ParkModal from './park-modale.vue'

  export default {
    name: 'Home',
    data() {
      return {
        revele: false,
        selectedParkingId: null,
      }
    },
    components: {
      'modale': ParkModal
    },
    methods: {
      toogleModale(parkingId) {
        this.selectedParkingId = parkingId
        this.revele = !this.revele
      },
      redirectReservation() {
        this.$router.push('/new-reservation')
      }
    },
    setup() {
      const parkings = ref([])
      const loading = ref(true)
      const error = ref(null)

      onMounted(async () => {
        try {
            const response = await fetch('http://localhost:8000/api/parkings')
            if (!response.ok) {
              throw new Error('Network response was not ok')
            }
          parkings.value = await response.json()
        } catch (err) {
            error.value = err.message
        } finally {
            loading.value = false
        }
      })

      return {
        parkings,
        loading,
        error,
      }
    }
  }
</script>

<style>
  h1 {
    color:#7D7D7D;
    font-size: 2em;
    font-weight: bolder;
    font-family: 'Lato';
  }

  .home-container {
    width: 100vw;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;  
  }

  .park-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }

  .park-box {
    display: flex;
    margin: 20px;
    padding: 20px;
    border: 1px solid #c4c4c4;
    border-radius: 5px;
    
  }

  .park-box p {
    font-family: 'Lato';
 
  }

  .park-box:hover {
    background-color: #FD8074;
    color: whitesmoke;
    cursor: pointer;
    transform: scale(1.2);
    box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
  }

  .new-resa-button {
    display: block;
    margin: 20px auto;
    padding: 10px 20px;
    background-color: #FD8074;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }

  .new-resa-button:hover {
    background-color: #f19890;
    transform: scale(0.95);
  }

</style>