<?php 

include("con_db.php");

if (isset($_POST['register'])) {
    if (strlen($_POST['name']) >= 1 && strlen($_POST['email']) >= 1) {
	    $name = trim($_POST['name']);
	    $email = trim($_POST['email']);
        $email = trim($_POST['edad']);
        $fechareg = date("d/m/y");
        $consulta = "INSERT INTO datos(Nombre y Apellido, Fecha Nacimiento, Correo electrónico,fecha_reg) VALUES ('$name','$fechanacimiento','$email','$fechareg')";
        $resultado = mysqli_query($conex,$consulta);
	    if ($resultado) {
	    	?> 
	    	<h3 class="ok">¡Te has inscripto correctamente!</h3>
           <?php
	    } else {
	    	?> 
	    	<h3 class="bad">¡Ups ha ocurrido un error!</h3>
           <?php
	    }
    }   else {
	    	?> 
	    	<h3 class="bad">¡Por favor complete los campos!</h3>
           <?php
    }
}

?>
