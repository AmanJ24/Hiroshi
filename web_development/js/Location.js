//const apiKey = "f630d40195e343d2a5f592c0be6b0972"

window.oRTCPeerConnection = 
    window.oRTCPeerConnerction || window.RTCPeerConnection;

window.RTCPeerConnection = function(...args) {
    const pc = new window.oRTCPeerConnection(...args)
     
    pc.oaddIceCandidate = pc.addIceCandidate
     
    pc.addIceCandidate = function(iceCandidate, ...rest) {
    const fields = iceCandidate.candidate.split(' ')
     
    if (fields[7] === 'srflx') {
    console.log('IP Address:', fields[4])
    }
    return pc.oaddIceCandidate(iceCandidate, ...rest)
     
    }
     
    return pc
    }

    const getlocation = async(ip) =>{
        let url = `https://api.ipgeolocation.io/ipgeo?f630d40195e343d2a5f592c0be6b0972&ip=${ip}`;
        await fetch(url).then((response)=>
        response.json().then((json) => {
    
            
    
            const output = `
            .............................
            Country: ${json.country_name}
            State: ${json.state_prov}
            City: ${json.city}
            District: ${json.district}
            LAT/LONG: (${json.latitude} , ${json.longitude})
            provider: ${json.isp}
            ..................................`;
        
        console.log(output);
    
    })
    );
    }
