// Alert on crush submission
document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    if (form && form.action.includes('/submit')) {
        form.addEventListener('submit', () => {
            alert("Your crush has been submitted 💌");
        });
    }

    // Style each mention with a random border color
    const colors = ['#ff69b4', '#87cefa', '#ffa07a', '#90ee90', '#dda0dd'];
    document.querySelectorAll('li').forEach(li => {
        const color = colors[Math.floor(Math.random() * colors.length)];
        li.style.borderLeft = `5px solid ${color}`;
    });
});
