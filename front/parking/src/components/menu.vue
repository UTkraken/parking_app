<template>
    <nav class="menu">
        <div class="menu-left">
            <div><RouterLink to="/">ParkDashboard</RouterLink></div>
        </div>
        <div class="menu-right">
            <div><RouterLink to="/reservation">Reservation</RouterLink></div>
            <div><RouterLink to="/login">Connexion</RouterLink></div>
        </div>
    </nav>
</template>

<script>
export default {
    name: "Menu",
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&display=swap');
nav {
  position:fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 200;
  height: 70px;
  border-bottom: 1px solid whitesmoke;
}

.menu {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.menu-left {
    margin-left: 2%;
}

.menu-left a {
    text-decoration: none;
    font-size: 1.2em;
    font-weight: bold;
    font-family: 'Lato';
    color: #7D7D7D;
}

.menu-right {
    display: flex;
    margin-right: 4%;
}

.menu-right div {
    margin-right: 10%;
}

.menu-right a {
    text-decoration: none;
    font-size: 1.2em;
    font-weight: bold;
    font-family: 'Lato';
    color: #7D7D7D;
}

.menu-left a:hover , .menu-right a:hover{
    color: #f19890;
}
</style>