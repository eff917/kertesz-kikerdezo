<svelte:head>
    <title>Teszt</title>
</svelte:head>

<script>
    import { plantData, plantList } from "../stores/plants";
    import { remainingPlants } from "../stores/lists";
import { goto } from "$app/navigation";

    let answerField;
    let answer = "";
    let plantListValue;
    plantList.subscribe(value => {
        plantListValue = value;
    })

    let plantDataValue;
    plantData.subscribe(dataValue => {
        plantDataValue = dataValue;
    })

    let remainingPlantsValue;
    remainingPlants.subscribe(value => {
        remainingPlantsValue = value;
    })

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

    let plant = selectPlant($remainingPlants);

    function checkAnswer(answer) {
        if (answer == plant) {
            const index = $remainingPlants.indexOf(answer);
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
        }
    };

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
<p class="m-auto">{plant}</p>
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
<p class="align-middle align-center">{plantDataValue[plant]['hungarianName']}</p>
{:else}
<button 
    on:click={() => handleClick("hun")}
    class="bg-yellow-300 hover:bg-yellow-500 text-gray-700 font-bold py-2 px-4 rounded"
    >Magyar név megjelenítése</button><br />
{/if}
</div>
<!-- Show images of the elected plant -->
</div>
{#if plantDataValue[plant]}
{#each plantDataValue[plant]['images'] as image}
<img src="http://192.168.88.247:8000/static/images/{image}" alt={plant}>
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