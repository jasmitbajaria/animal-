// Main JavaScript for Animal Encyclopedia

document.addEventListener('DOMContentLoaded', function() {
    // Initialize habitat navigation
    initHabitatNavigation();
    
    // Initialize modal functionality
    initModalFunctionality();
});

function initHabitatNavigation() {
    document.querySelectorAll('.habitat-btn').forEach(button => {
        button.addEventListener('click', function() {
            const habitat = this.getAttribute('data-habitat');
            
            // Update active button
            document.querySelectorAll('.habitat-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            this.classList.add('active');
            
            // Update visible content
            document.querySelectorAll('.habitat-content').forEach(content => {
                content.classList.remove('active');
            });
            document.getElementById(habitat).classList.add('active');
        });
    });
}

function initModalFunctionality() {
    // Close modal when clicking the close button or outside the modal
    document.querySelectorAll('.close, .modal').forEach(element => {
        element.addEventListener('click', function(e) {
            if (e.target === this) {
                document.getElementById('animalModal').style.display = 'none';
            }
        });
    });

    // Initialize tab functionality
    document.querySelectorAll('.tab-btn').forEach(button => {
        button.addEventListener('click', function() {
            // Update active button
            document.querySelectorAll('.tab-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            this.classList.add('active');
            
            // Update visible content
            const contentId = this.id.replace('Tab', 'Content');
            document.querySelectorAll('.tab-content').forEach(content => {
                content.classList.remove('active');
            });
            document.getElementById(contentId).classList.add('active');
        });
    });
}

function showAnimalModal(animalId, section) {
    // Show loading state
    const modal = document.getElementById('animalModal');
    modal.style.display = 'block';
    
    // Fetch animal data
    fetch(`/api/animal/${animalId}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Update modal content based on section (kids or scholars)
            updateModalContent(data, section);
        })
        .catch(error => {
            console.error('Error fetching animal data:', error);
            // Show error message in modal
            document.querySelector('.modal-content').innerHTML = `
                <span class="close">&times;</span>
                <div class="error-message">
                    <h2>Oops! Something went wrong</h2>
                    <p>We couldn't fetch the animal information. Please try again later.</p>
                </div>
            `;
        });
}

function updateModalContent(data, section) {
    // Update common elements
    document.getElementById('modalAnimalName').textContent = data.name;
    
    // Update images
    updateModalImages(data);
    
    // Update audio if available
    updateModalAudio(data);
    
    if (section === 'kids') {
        updateKidsContent(data);
    } else {
        updateScholarsContent(data);
    }
}

function updateModalImages(data) {
    const images = ['modalImage1', 'modalImage2', 'modalImage3'];
    images.forEach((imgId, index) => {
        const img = document.getElementById(imgId);
        const imageKey = `image${index + 1}`;
        if (data[imageKey]) {
            img.src = data[imageKey];
            img.style.display = 'block';
        } else {
            img.style.display = 'none';
        }
    });
}

function updateModalAudio(data) {
    const audioSection = document.getElementById('audioSection');
    const audio = document.getElementById('animalAudio');
    const description = document.getElementById('audioDescription');
    
    if (data.audio) {
        audio.src = data.audio;
        description.textContent = data.audio_description || '';
        audioSection.style.display = 'block';
    } else {
        audioSection.style.display = 'none';
    }
}

function updateKidsContent(data) {
    // Update description for kids
    document.querySelector('.modal-description').innerHTML = data.description_kids;
    
    // Update fun facts
    document.getElementById('funFacts').innerHTML = data.fun_facts_kids;
    
    // Update habitat info
    document.getElementById('habitatInfo').innerHTML = data.habitat_info_kids;
    
    // Update behavior info
    document.getElementById('behaviorInfo').innerHTML = data.behavior_info_kids;
    
    // Update conservation status
    document.getElementById('conservationStatus').innerHTML = data.conservation_status_kids;
}

function updateScholarsContent(data) {
    // Update scientific name
    document.getElementById('modalScientificName').textContent = data.scientific_name;
    
    // Update detailed content for scholars
    document.querySelector('.modal-description').innerHTML = data.description_scholars;
    document.getElementById('anatomyInfo').innerHTML = data.anatomy_info || '';
    document.getElementById('habitatInfo').innerHTML = data.habitat_info;
    document.getElementById('behaviorInfo').innerHTML = data.behavior_info;
    document.getElementById('conservationStatus').innerHTML = data.conservation_status;
    document.getElementById('researchInfo').innerHTML = data.research_info || '';
}

// Error handling helper
function handleError(error, element) {
    console.error(error);
    element.innerHTML = `
        <div class="error-message">
            <p>Sorry, we couldn't load this content. Please try again later.</p>
        </div>
    `;
}
