file "build/out.epub" => FileList['rst/*.rst'] do
	mkdir_p "build"
	sh 'echo "Worm.\n=====\n\nparahumans.wordpress.com\n------------------------\n" > rst/0.0_Title.rst'
	sh "txt2epub build/out.epub rst/*.rst --title=Worm --creator=parahumans.wordpress.com"
end

task :compile => ["build/out.epub"]

task :default => [:compile]