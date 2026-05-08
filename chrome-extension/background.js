chrome.history.onVisited.addListener(async (result) => {

    const url = result.url;

    let memoryText = null;

    // GOOGLE SEARCH
    if (url.includes("google.com/search?q=")) {

        const query = new URL(url)
            .searchParams
            .get("q");

        memoryText = `User searched Google for ${query}`;
    }

    // YOUTUBE SEARCH
    else if (
        url.includes("youtube.com/results?search_query=")
    ) {

        const query = new URL(url)
            .searchParams
            .get("search_query");

        memoryText = `User searched YouTube for ${query}`;
    }

    // AMAZON SEARCH
    else if (
        url.includes("amazon")
        && url.includes("k=")
    ) {

        const query = new URL(url)
            .searchParams
            .get("k");

        memoryText = `User searched Amazon for ${query}`;
    }

    // Ignore unrelated websites
    if (!memoryText) {
        return;
    }

    console.log(memoryText);

    try {

        await fetch(
            "http://127.0.0.1:8000/add-memory",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    text: memoryText
                })
            }
        );

        console.log("Memory stored");

    } catch (error) {

        console.log(error);

    }

});