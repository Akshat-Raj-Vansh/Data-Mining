<!DOCTYPE html>
<html>

<head>
    <title>LAB ASSIGNMENT 7</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * {
            box-sizing: border-box;
        }
        
        .column {
            float: none;
            width: 80%;
            padding: 10px;
            height: 300px;
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
            <legend>DATA MINING AND WAREHOUSING LAB ASSIGNMENT 7</legend>
            <center>
                <ul>
                    <label for="files">File : </label>
                    <input type="file" id="files" name="files" multiple />
                </ul>
                <ul>Weights:
                    <input name="weights" /></ul>
                <ul>Impact:
                    <input name="impact" /></ul>
                <ul>Email:
                    <input name="email" /></ul>
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
    </div>

</body>

</html>