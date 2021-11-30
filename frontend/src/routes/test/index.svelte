<svelte:head>
    <title>Teszt</title>
</svelte:head>

<script>
    import { remainingPlants } from "../../stores/lists";
    import { goto } from "$app/navigation";

    let answerField;
    let answer = "";

    let remainingPlantsValue;
    remainingPlants.subscribe(value => {
        remainingPlantsValue = value;
    })
    console.log(remainingPlantsValue)


    let showLatinName = false;
    let showHungarianName = false;

    function handleClick(name) {
        if (name === "latin") {
            showLatinName = true;
        };
        if (name === "hun") {
            showHungarianName = true;
        }
    }
    console.log($remainingPlants)
    
    function selectPlant(plantList) {
        return plantList[Math.floor(Math.random()*plantList.length)];
    }
    
    function checkAnswer(answer) {
        
        if (answer == plant.latin_name) {
            const index = $remainingPlants.indexOf(plant);
            console.log(index)
            answer='';
            answerField.value = '';
            if (index > -1) {
                $remainingPlants.splice(index, 1);
                $remainingPlants = $remainingPlants;
            }
            plant = selectPlant($remainingPlants)
            showHungarianName = false;
            showLatinName = false;
            console.log($remainingPlants)
            console.log(remainingPlantsValue)
        }
    };

    let plant = selectPlant($remainingPlants);
    console.log(plant)

</script>


{#if remainingPlantsValue.length > 0}
    <p>Hátralevő növények száma:  {remainingPlantsValue.length}</p>
    <form on:submit|preventDefault={() => checkAnswer(answer)}>
        <input 
            bind:value={answer} 
            bind:this={answerField}
            class="border-2 border-black rounded"
        >
        <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" type="submit">
            Ellenőrzés
        </button>
    </form>
    <!-- Toggle latin name of the plant -->
    <div class="h-20 m-auto">
        <div class="h-10 m-auto">
            {#if showLatinName}
                <p class="m-auto">{plant.latin_name}</p>
            {:else}
                <button 
                    on:click={() => handleClick("latin")}
                    class="bg-yellow-300 hover:bg-yellow-500 text-gray-700 font-bold py-2 px-4 rounded"
                >Latin név megjelenítése</button><br />
            {/if}
        </div>
    <!-- Toggle hungarian name of the plant -->
    <div class="h-10 align-middle align-center">
    {#if showHungarianName}
        <p class="align-middle align-center">{plant.hungarian_name}</p>
    {:else}
        <button 
            on:click={() => handleClick("hun")}
            class="bg-yellow-300 hover:bg-yellow-500 text-gray-700 font-bold py-2 px-4 rounded"
            >Magyar név megjelenítése
        </button>
        <br />
    {/if}
</div>
<!-- Show images of the selected plant -->
</div>
{#if plant}
{#each plant.pictures as image}
<img src={image.path} alt={plant.latin_name}>
{/each}
{/if}
{:else}
<p>Vége!</p>
<button 
    on:click={() => {goto("/lists")}} 
    class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
>Lista kiválasztása új teszthez</button>
{/if}

<style>
    img {
        max-width: 90vw;
        max-height: 90vh;
    }
</style>