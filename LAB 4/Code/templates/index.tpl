<!DOCTYPE html>
<html>
<head>
    <title>LAB ASSIGNMENT 4</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
  box-sizing: border-box;
}
.column {
  float: left;
  width: 50%;
  padding: 10px;
  height: 600px; 
   overflow-x: hidden;
            overflow-y: auto;
            text-align: justify;
}

.row:after {
  content: "";
  display: table;
  clear: both;
}
    </style>
</head>

<body>
    <form method="post" action="/">
        <fieldset>
            <legend>DATA MINING AND WAREHOUSING LAB ASSIGNMENT 4</legend>
            <center>
                <ul>
                    <label for="files">Select files : </label>
                    <input type="file" id="files" name="files" multiple /> Email ID:
                    <input name="first" />
                </ul>

                <input type="submit" value="Generate Result" />
            </center>
        </fieldset>
    </form>
    <br />

</div>
 <div class="row">
  <div class="column" style="background-color:#aaa;">
    <h2>{{resultname}}</h2>
    <p>{{result}}</p>
  </div>
  <div class="column" style="background-color:#bbb;">
    <h2>{{logname}}</h2>
    <p>{{log}}</p>
  </div>
</div>
        
</body>

</html>