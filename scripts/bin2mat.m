idx = [1 2];
inFilenames = "ism24gfulls" + idx + ".ota.rx.r001";
outFilename = "ism24gfulls.ota.rx.r001";

data = zeros(1e8, length(idx));

for i = idx
    fileID = fopen(sprintf("%s.sigmf-data", inFilenames(i)), "r");
    in = fread(fileID, [2 inf], "*float32");
    fclose(fileID);
    data(:, i) = complex(in(1, :), in(2, :))';
end

save(sprintf("%s.mat", outFilename), "data", "-v7.3")
