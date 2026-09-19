using Plots 
using LaTeXStrings

function compute_area_of_circle(n)
    cover::Int = 0
    for i in -n:n
        for j in -n:n
            if ((i/n)^2 + (j/n)^2) < 1
                if i == 0 && j == 0
                    cover += 4
                elseif i == 0 || j == 0 
                    cover += 2
                else 
                    cover += 1
                end 
            end
        end
    end
    return cover * (1/n)^2
end 

function main()
    ns = 1:1:100
    println(ns)
    areas = compute_area_of_circle.(ns)
    plot(ns, areas, 
        label=L"\sum_{j=1}^{4n^2}|A_j|",
        title="Approximated Outer-measure of Unit Circle", 
        xlabel="Resolution", ylabel="Area",
        dpi=300
    )

    plot!(ns, ones(100)*π, 
        label=L"\mu^*")

    dir = dirname(dirname(@__FILE__))
    savefig(joinpath(dir, "media/outer_measure_of_unit_circle.png"))
end 

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end