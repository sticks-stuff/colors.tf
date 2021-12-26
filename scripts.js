// return JSON data from any file path (asynchronous)
function getJSON(path) {
    return fetch(path).then(response => response.json());
}

// document.getElementById('red').addEventListener("change", watchColorPickerRed, false);
// document.getElementById('blue').addEventListener("change", watchColorPickerBlue, false);

// function watchColorPickerRed(event) {
//     watchColorPicker(event, "red")
// }

// function watchColorPickerBlue(event) {
//     watchColorPicker(event, "blue")
// }

function watchColorPicker(hex, team) {
	color = hexToRgb(hex);
	
    if(team == "red") {
        originalHSL = rgbToHsl(204, 20, 13); //god i love hard coding vars
        critColor = document.querySelectorAll('[jsonpath="material,red_crit,color"]')[0]
    } else {
        originalHSL = rgbToHsl(13, 51, 204);
        critColor = document.querySelectorAll('[jsonpath="material,blue_crit,color"]')[0]
    }

	colorHSL = rgbToHsl(color[0], color[1], color[2])
	var newColorDiff = [];
	newColorDiff[0] = colorHSL[0] - originalHSL[0];
	newColorDiff[1] = colorHSL[1] - originalHSL[1];
	newColorDiff[2] = colorHSL[2] - originalHSL[2];
	// console.log({originalHSL})
	// console.log({colorHSL})
	// console.log({newColorDiff})
	Array.from(document.getElementsByClassName(`${team}-particle`)).forEach(element => {
		Array.from(element.getElementsByClassName('colour-display')).forEach(element => {
			originalColor = element.attributes.ogcolour.value;
			// originalColor = originalColor.slice(10, -1);
            // console.log(originalColor)
			originalColor = originalColor.split(' ');
			originalColorHSL = rgbToHsl(originalColor[0], originalColor[1], originalColor[2]);
			// console.log({originalColorHSL})
			originalColorHSL[0] += newColorDiff[0];
			originalColorHSL[1] += newColorDiff[1];
			originalColorHSL[2] += newColorDiff[2];
			originalColor = hslToRgb(originalColorHSL[0], originalColorHSL[1], originalColorHSL[2]);
			element.style.backgroundColor = 'rgb(' + originalColor.join(', ') + ')';
		});
	});

    // critColorRGB = critColor.style.backgroundColor.slice(4, -1);
    // critColorRGB = critColorRGB.split(', ');
    // console.log({critColorRGB})
    // console.log(parseInt(critColorRGB[0]), parseInt(critColorRGB[1]), parseInt(critColorRGB[2]));
    // critColorHSL = rgbToHsl(parseInt(critColorRGB[0]), parseInt(critColorRGB[1]), parseInt(critColorRGB[2]));
    // console.log({critColorHSL})

    // critColorHSL[0] -= 0.05;
    // critColorHSL[1] -= 0.05;
    // from my testing take 10 away from hue and sat to get in game color
    // critColorHSL = hslToRgb(critColorHSL[0], critColorHSL[1], critColorHSL[2]);

    // console.log({critColorHSL})

    if(team == "red") {
        document.getElementById('preview-color-red').style.backgroundColor = critColor.style.backgroundColor;
        // document.getElementById('preview-color-red').style.backgroundColor = 'rgb(' + critColorHSL.join(', ') + ')';
    } else {
        document.getElementById('preview-color-blu').style.backgroundColor = critColor.style.backgroundColor;
        // document.getElementById('preview-color-blu').style.backgroundColor = 'rgb(' + critColorHSL.join(', ') + ')';
    }
}

function hexToRgb(hex) {
	var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
	if(result){
		var r= parseInt(result[1], 16);
		var g= parseInt(result[2], 16);
		var b= parseInt(result[3], 16);
		return [r, g, b];
	} 
	return null;
}

/**
 * Converts an HSL color value to RGB. Conversion formula
 * adapted from http://en.wikipedia.org/wiki/HSL_color_space.
 * Assumes h, s, and l are contained in the set [0, 1] and
 * returns r, g, and b in the set [0, 255].
 *
 * @param   {number}  h       The hue
 * @param   {number}  s       The saturation
 * @param   {number}  l       The lightness
 * @return  {Array}           The RGB representation
 */
 function hslToRgb(h, s, l){
    var r, g, b;

    if(s == 0){
        r = g = b = l; // achromatic
    }else{
        var hue2rgb = function hue2rgb(p, q, t){
            if(t < 0) t += 1;
            if(t > 1) t -= 1;
            if(t < 1/6) return p + (q - p) * 6 * t;
            if(t < 1/2) return q;
            if(t < 2/3) return p + (q - p) * (2/3 - t) * 6;
            return p;
        }

        var q = l < 0.5 ? l * (1 + s) : l + s - l * s;
        var p = 2 * l - q;
        r = hue2rgb(p, q, h + 1/3);
        g = hue2rgb(p, q, h);
        b = hue2rgb(p, q, h - 1/3);
    }

    return [Math.round(r * 255), Math.round(g * 255), Math.round(b * 255)];
}

/**
 * Converts an RGB color value to HSL. Conversion formula
 * adapted from http://en.wikipedia.org/wiki/HSL_color_space.
 * Assumes r, g, and b are contained in the set [0, 255] and
 * returns h, s, and l in the set [0, 1].
 *
 * @param   {number}  r       The red color value
 * @param   {number}  g       The green color value
 * @param   {number}  b       The blue color value
 * @return  {Array}           The HSL representation
 */
 function rgbToHsl(r, g, b){
    r /= 255, g /= 255, b /= 255;
    var max = Math.max(r, g, b), min = Math.min(r, g, b);
    var h, s, l = (max + min) / 2;

    if(max == min){
        h = s = 0; // achromatic
    }else{
        var d = max - min;
        s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
        switch(max){
            case r: h = (g - b) / d + (g < b ? 6 : 0); break;
            case g: h = (b - r) / d + 2; break;
            case b: h = (r - g) / d + 4; break;
        }
        h /= 6;
    }

    return [h, s, l];
}

function mod (n, m) {
    var remain = n % m;
    return Math.floor(remain >= 0 ? remain : remain + m);
}

function modifyJSON() {
    getJSON('output.json').then(data => {
        Array.from(document.getElementsByClassName('colour-display')).forEach(element => {
            jsonPath = element.attributes.jsonpath.value;
            jsonPath = jsonPath.split(',');
            jsonElement = data[jsonPath[0]][jsonPath[1]][jsonPath[2]];

            newColor = element.style.backgroundColor;
			newColor = newColor.substring(4).slice(0, -1);
			newColor = newColor.split(', ');

            jsonElement[0] = newColor[0];
            jsonElement[1] = newColor[1];
            jsonElement[2] = newColor[2];
        });
        console.log(data);
        xhr.open("POST", url, true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.send(JSON.stringify(data));
    })    
}

var xhr = new XMLHttpRequest();
var url = "http://127.0.0.1:3000/generate";
xhr.responseType = "blob";

xhr.onreadystatechange = function() {
    console.log(xhr.readyState)
    console.log(xhr.status)
    if(xhr.readyState == 4) {
        var blob = xhr.response;
        var fileName = xhr.getResponseHeader('content-disposition').split('filename=')[1].split(';')[0];
        var link=document.createElement('a');
        link.href=window.URL.createObjectURL(blob);
        link.download=fileName;
        link.click();
    }
}  

function previewSelect(team) {
    if(team == 'red') {
        document.getElementById('preview-color-blu').style.display = 'none';
        document.getElementById('preview-color-red').style.display = 'revert';
        document.getElementById('preview-hand-blu').style.display = 'none';
        document.getElementById('preview-hand-red').style.display = 'revert';
    } else {
        document.getElementById('preview-color-red').style.display = 'none';
        document.getElementById('preview-color-blu').style.display = 'revert';
        document.getElementById('preview-hand-red').style.display = 'none';
        document.getElementById('preview-hand-blu').style.display = 'revert';
    }
}

Array.from(document.getElementsByClassName('colour-display')).forEach(element => {
    picker = new CP(element);
    disableAlphaControl(picker);
    // console.log({rgbColorofEl});
    picker.on('enter', function(r, g, b, a) {
        rgbColorofEl = this.source.style.backgroundColor.slice(4, -1).split(', ');
        this.set(parseInt(rgbColorofEl[0]), parseInt(rgbColorofEl[1]), parseInt(rgbColorofEl[2]), 1);
    });
    picker.on('drag', function(r, g, b, a) {
        this.source.style.backgroundColor = this.color(r, g, b, a);
    });
    picker.on('exit', function(r, g, b, a) {
        this.set(this.color(r, g, b, a))
    });
    if(element.attributes.jsonpath.value == "material,red_crit,color") {
        picker.on('drag', function(r, g, b, a) {
            this.source.style.backgroundColor = this.color(r, g, b, a);
            watchColorPicker(CP.HEX([r, g, b]), 'red') //yes i turn RGB into a hex color only to turn it back into RGB stop asking so many questions
        });
    }
    if(element.attributes.jsonpath.value == "material,blue_crit,color") {
        picker.on('drag', function(r, g, b, a) {
            this.source.style.backgroundColor = this.color(r, g, b, a);
            watchColorPicker(CP.HEX([r, g, b]), 'blue')
        });
    }
});

function disableAlphaControl(picker) {
    if (picker.noAlpha) {
        return;
    }
    picker.noAlpha = true;
    picker.self.classList.add('no-alpha');
    picker.on('change', function(r, g, b) {
        this.source.value = this.color(r, g, b, 1);
    });
}
