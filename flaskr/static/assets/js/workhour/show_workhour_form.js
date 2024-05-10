// This file allow to insert all the fields down, all the time the button is clicked

// Create a counter variable to keep track of the number of form fields added
var counter = 0;

// Get a reference to the field container element
var workhourFieldsContainer = document.getElementById('WorkhourFieldsContainer');

// Add an event listener to the button that will be triggered when it is clicked
document.getElementById('workhourFormButton').addEventListener('click', function () {
    // Increment the counter variable
    counter++;

    // Create a new form field element
    var newField = document.createElement('div');

    // Set the inner HTML of the new form field to a text input with a unique name and placeholder
    newField.innerHTML = `
  <div class="row">
    <div class="col-md-6">


<div class="form-group row">
<label for="vertical_${counter}" class="col-sm-3 col-form-label">Verticale</label>
<div class="col-sm-9">
    <select type="time" name="vertical_${counter}" class="form-control form-control-sm">
        <option value="-">-</option>
        <option value="Lunedi">Lunedi</option>
        <option value="Martedi">Martedi</option>
        <option value="Mercoledi">Mercoledi</option>
        <option value="Giovedi">Giovedi</option>
        <option value="Venerdi">Venerdi</option>
        <option value="Sabato">Sabato</option>
    </select>
</div>
</div>


        
        <div class="form-group row">
            <label for="from_hours_${counter}" class="col-sm-3 col-form-label">Dalle</label>
            <div class="col-sm-9">
                <input type="time" name="from_hours_${counter}" class="form-control form-control-sm"  />
            </div>
        </div>

       
    </div>
    
    <div class="col-md-6">
       

    <div class="form-group row">
    <label for="horizontal_${counter}" class="col-sm-3 col-form-label">Orizontale</label>
    <div class="col-sm-9">
        <select type="time" name="horizontal_${counter}" class="form-control form-control-sm">
            <option value="-">-</option>
            <option value="mattina">mattina</option>
            <option value="pomeriggio">pomeriggio</option>
            <option value="notte">notte</option>
        
        </select>
    </div>
    </div>

        <div class="form-group row">
        <label for="to_hours_${counter}" class="col-sm-3 col-form-label">Alle</label>
        <div class="col-sm-9">
            <input type="time" name="to_hours_${counter}" class="form-control form-control-sm"/>
        </div>
    </div>


    </div>
  </div>
  <hr class="hr-bold">
  `;

    // Append the new form field to the field container element
    workhourFieldsContainer.appendChild(newField);
});

