<template>
    <div class="reservation-container">
      <h1>New reservation</h1>
      <form @submit.prevent="onSubmitform">
        <div class="form-group">
            <label for="date">Date</label>
            <input type="date" id="date" name="date" required v-model="reservation.date">
        </div>
        <div class="form-group">
            <label for="parking">Parking</label>
            <select id="parking" name="parking" required v-model="reservation.parking_id">
                <option v-for="parking in parkings" :key="parking.id" :value="parking.id">{{ parking.name }}</option>
            </select>
        </div>
        <button>Validate</button>
      </form>
    </div>
  </template>
  
  <script>
    import axios from 'axios'
    import { ref, onMounted } from 'vue'
    import { useToast } from 'vue-toastification'
    import { useRoute } from 'vue-router'
  const toast = useToast()

  export default {
    name: 'ReservationForm',
    data() {
        return {
            reservation: {
                date: null,
                parking_id: null,
            },
        }
    },
    methods: {
        onSubmitform() {
            if (this.isEdit) {
                axios.put(`http://localhost:8000/api/reservations/${this.route.params.id}`, this.reservation)
                .then(response => {
                    toast.success('Reservation updated successfully!')
                    this.$router.push('/')
                })
                .catch(error => {
                    toast.error('Error updating reservation')
                })
            } else {
                axios.post('http://localhost:8000/api/reservations', this.reservation)
                .then(response => {
                    toast.success('Reservation created successfully!')
                    this.$router.push('/')
                })
                .catch(error => {
                    toast.error('Error creating reservation')
                })
            }
        },
    },
    setup() {
      const parkings = ref([])
      const loading = ref(true)
      const error = ref(null)
      const route = useRoute()
      const isEdit = ref(false)
      const reservation = ref({
        date: null,
        parking_id: null,
      })
      

    onMounted(async () => {
        try {
            const response = await fetch('http://localhost:8000/api/parkings')
            if (!response.ok) {
                throw new Error('Network response was not ok')
            }
            parkings.value = await response.json()

            if (route.params.id) {
                isEdit.value = true
                const res = await axios.get(`http://localhost:8000/api/reservations/${route.params.id}`)
                reservation.value = {
                    date: res.data.date,
                    parking_id: res.data.parking.id,
                }
            }

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
        reservation,
        isEdit,
        route,
    }
    },
  }
  </script>

<style scoped>

    h1 {
        color:#7D7D7D;
        font-size: 2em;
        font-weight: bolder;
        font-family: 'Lato';
        margin-bottom: 5%;
    }

    .reservation-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
    }
    
    .form-group {
        margin-bottom: 20px;
    }
    
    .form-group label {
        display: block;
        margin-bottom: 5px;
        font-family: 'Lato';
        color: #7D7D7D;
    }
    
    .form-group input,
    .form-group select {
        width: 200px;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #ccc;
    }
    
    button {
        padding: 10px 20px;
        background-color: #FD8074;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
</style>