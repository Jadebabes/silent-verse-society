function summonPoem() {
    const prompt = document.getElementById("promptInput").value.toLowerCase();
    const result = document.getElementById("poemResult");

    const poems = {
        love: "A rose did bloom in ruin's bed,\nYet thorns were all the words she said.",
        sorrow: "The moon weeps not, and yet I know—\nShe mourns the light I cannot show.",
        madness: "I kissed the edge of reason's blade,\nAnd called it muse beneath the shade.",
        default: "From silence born, in ink I bled—\nTo write the truths none ever said."
    };

    if (poems[prompt]) {
        result.textContent = poems[prompt];
    } else {
        result.textContent = poems["default"];
    }
}
