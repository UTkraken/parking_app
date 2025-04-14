<template>
  <div>
    <park-modale :revele="revele" :toggleModale="toogleModale" :parking-id="selectedParkingId" @modaleStatus="printStatus"></park-modale>
    <div v-if="loading" class="loading">Loading...</div>
    <div v-else-if="error">Error: {{ error }}</div>
    <div v-else class="home-container">
      <h1>Available Parking</h1>
      <div class="park-container">
        <div class="picker">
          <input type="date" v-model="date">
        </div>
        <div class="box-container">
          <div class="park-box" v-on:click="toogleModale(parking.id)" v-for="parking in parkings" :key="parking.id">
            <div class="info-park">
              <div>{{ parking.name }}</div>
              <div>Available spots: {{ parking.available_spots_count }}</div>
            </div>
          </div>
        </div> 
      </div>
      <button v-on:click="redirectReservation" class="new-resa-button">New reservation</button>
    </div>
  </div>
</template>
  
<script>
  import { ref, onMounted, watch } from 'vue'
  import ParkModal from './park-modale.vue'
  import DatePicker from 'primevue/datepicker'
  import axios from 'axios'
  import { useToast } from 'vue-toastification'

  const toast = useToast()

  export default {
    name: 'Home',
    data() {
      return {
        revele: false,
        selectedParkingId: null,
      }
    },
    components: {
      'park-modale': ParkModal,
      'datePicker': DatePicker
    },
    methods: {
      toogleModale(parkingId) {
        this.selectedParkingId = parkingId
        this.revele = !this.revele
      },
      redirectReservation() {
        this.$router.push('/new-reservation')
      },
      printStatus(data) {
        console.log('Modale Status: ' + data)
      }
    },
    setup() {
      const parkings = ref([])
      const loading = ref(true)
      const error = ref(null)
      const date = ref(new Date())

      const updateParkings = async () => {
        loading.value = true
        error.value = null
        const formattedDate = new Date(date.value).toISOString().split('T')[0]
        try {
          const response = await axios.get(`http://localhost:8000/api/parkings?date=${formattedDate}`)
          parkings.value = response.data
          toast.success('Parkings updated!')
        } catch (err) {
          error.value = err.response?.data?.message || 'Erreur de chargement'
          toast.error('Error: ' + error.value)
        } finally {
          loading.value = false
        }
      }

      onMounted(updateParkings)

      watch(date, () => {
        updateParkings()
      })

      return {
        parkings,
        loading,
        error,
        date,
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
    margin-top: 2%;
    margin-bottom: 2%;
  }

  .home-container, .loading {
    width: 100vw;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;  
    font-family: 'Lato';
    color:#7D7D7D;
  }

  .park-container {
    justify-content: center;
  }

  .park-box {
    display: flex;
    margin: 20px;
    padding: 20px;
    border: 1px solid #c4c4c4;
    border-radius: 5px;
    flex-direction: column;
    justify-content: center;
    align-items: center;

  }

  .park-box div {
    font-family: 'Lato';
  }

  .park-box:hover {
    background-color: #FD8074;
    color: whitesmoke;
    cursor: pointer;
    transform: scale(1.2);
    box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
  }

  .info-park {
    text-align: center;
  }

  .info-park > div {
    margin-bottom: 5%;
    font-weight: 700;
  }

  .box-container {
    display: flex;
  }

  input {
    border: none;
    font-family: 'Lato';
    color: #7D7D7D;
    
  }

  .picker {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 30%;
    margin-left: 35%;
    max-width: 350px;
    height: 25px;
    border-bottom: 1px solid #f19890;
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