var express = require('express');
var compression = require('compression');
var app = express();

var PORT = 3000;
const path = require('path');
const router  = express.Router();
app.use(compression());
app.use(express.static('./'));

router.get('/', function(req, res) {
    res.sendFile(path.join(__dirname+'/index.html'));
});

app.use('/',router);

app.listen(PORT, function() {
    console.log('Server is running on PORT:',PORT);
});
