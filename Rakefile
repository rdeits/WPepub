file "build/out.epub" => FileList["rst/01.01_Gestation_1.1.rst"] do
	mkdir_p "build"
	sh 'echo "Worm.\n=====\n\nparahumans.wordpress.com\n------------------------\n" > rst/0.0_Title.rst'
	sh "txt2epub build/out.epub rst/*.rst --title=Worm --creator=parahumans.wordpress.com"
end


mirror_fname = "mirror/category/stories-arcs-1-10/arc-1-gestation/1-01/index.html"
file mirror_fname do
	Dir.chdir("WPepub") do
		sh "python scrape.py"
	end
end

file "rst/01.01_Gestation_1.1.rst" => [mirror_fname] do
	Dir.chdir("WPepub") do
		sh "python convert.py"
	end
end

task :compile => ["build/out.epub"]

task :default => [:compile]