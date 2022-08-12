//Create dynamic minimum and maximum input box.
/*

options explain
if the first number of the option is

0 == if auto generate is clicked then section (E, M, H) will show up.

1 == only min and max input will turning into block or none.

2 == only difficulty and number of problem will show up.

*/
function validate(id, opt) {
    var nid = id.charAt(id.length-1)

    if(document.getElementById('min' + nid).style.display != 'none') {
      document.getElementById('min' + nid).style.display = 'none';
      document.getElementById('max' + nid).style.display = 'none';
      document.getElementById('mint' + nid).style.display = 'none';
      document.getElementById('maxt' + nid).style.display = 'none';
      if(opt == 0) {
      document.getElementById('level' + nid).style.display = 'block';
      }
    } else {
      document.getElementById('min' + nid).style.display = 'block';
      document.getElementById('max' + nid).style.display = 'block';
      document.getElementById('mint' + nid).style.display = 'block';
      document.getElementById('maxt' + nid).style.display = 'block';
      if(opt == 0) {
      document.getElementById('level' + nid).style.display = 'none';
      }
    }
}

function dynamicSelection(list) {
    var label = document.createElement("label");
    label.className = "num-problem-font";
    label.textContent = "Learning Target*";
    document.getElementById("select").appendChild(label);

    var select = document.createElement("select");
    select.id = 'Ltarget';
    select.name = 'Ltarget1';
    select.value = 0;
    for(let i = 0; i < list.length; i++) {
        select.innerHTML += '<option value="' + (i+1) + '">' + list[i] + '</option>';
    }
    select.required = "True";
    document.getElementById("select").appendChild(select);
}

function dynamicDifficulty(list, opt) {
    var label = document.createElement("label");
    label.className = "auto-num-problem-font";
    label.textContent = "Section Field*";
    document.getElementById("level").appendChild(label);

    var select = document.createElement("select");
    select.id = "levels";
    select.name = "level1";
    select.className = "resizeinput";
    select.style = "margin-left: 10px";
    select.required = "True";
    for(let i = 0; i < list.length; i++) {
        select.innerHTML += '<option value="' + (i+1) + '">' + list[i] + '</option>';
    }

    document.getElementById("level").appendChild(select);
    if(opt == 0) {
        document.getElementById("level").style.display = "none";
    }
}

//Changing instructions
function displayinst(data, des) {
    for(let i = 0; i < total; i++) {
        document.getElementById("subpdfdesc" + (i+1)).innerText = data[des[i]];
    }
    changecol(wkst);
}