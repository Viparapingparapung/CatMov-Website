function data(result) {
    for (var i = 0; i < 10; i += 1) {
        // long = result.data[i].length
        let str = result.data[i]
        str = str.slice(0, -6)

        fetch(`https://api.themoviedb.org/3/search/movie?api_key=0b4a78f3f6df40ca3779248e701f90e5&language=&query=${str}&page=&include_adult=false`)
            .then(response => response.json())
            .then(result => console.log(result.results[0], result.results.length))
            .catch(error => console.log('error', error));

    }
}




fetch("https://iimispu82i.ap-northeast-1.awsapprunner.com/items/?rating=5&movie=Toy Story (1995)")
    .then(response => response.json())
    .then(result => data(result))
    .catch(error => console.log('error', error));


